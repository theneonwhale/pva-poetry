from abc import abstractmethod, ABC

from .address_book import AddressBook

import colorama
from colorama import Fore, Style
colorama.init()


class OutputInterface(ABC):
    @abstractmethod
    def create_output(self) -> str:
        pass


class ContactsOutput(OutputInterface):
    LIMIT = 5

    def create_output(self, contact_dictionary: AddressBook) -> str:
        for records in contact_dictionary.iterator(self.LIMIT):
            contact_message = ''
            for record in records:
                contact_message += Fore.MAGENTA + '{:-^10}\nName: '.format('') + Fore.LIGHTCYAN_EX + '{}\n{:-^10}\n'.format(f'{record.name.value}', '') + \
                                  Style.RESET_ALL

                if record.phones:
                    contact_message += Fore.WHITE + 'Phone(s): ' + Style.RESET_ALL
                    phones = ', '.join([phone.value for phone in record.phones])
                    contact_message += Fore.GREEN + f'{phones}' + Style.RESET_ALL
                else:
                    contact_message += Fore.WHITE + 'Phone(s): ' + Style.RESET_ALL
                    contact_message += Fore.YELLOW + 'empty' + Style.RESET_ALL

                if record.emails:
                    contact_message += Fore.WHITE + '\nEmail(s): ' + Style.RESET_ALL
                    emails = ', '.join([email.value for email in record.emails])
                    contact_message += Fore.GREEN + f'{emails}\n' + Style.RESET_ALL
                else:
                    contact_message += Fore.WHITE + '\nEmail(s): ' + Style.RESET_ALL
                    contact_message += Fore.YELLOW + 'empty\n' + Style.RESET_ALL

                contact_message += Fore.MAGENTA + '{:-^10}\n\n'.format('') + Style.RESET_ALL
        return contact_message


class ContactOutput(OutputInterface):
    def create_output(self, name: str, contact_dictionary: AddressBook) -> str:
        message_to_user = Fore.MAGENTA + '{:-^10}\nName: '.format('') + Fore.LIGHTCYAN_EX + \
                      '{}\n{:-^10}\n'.format(f'{name}', '') + Style.RESET_ALL

        if contact_dictionary[name].phones:
            message_to_user += Fore.WHITE + 'Phone(s): ' + Style.RESET_ALL
            message_to_user += Fore.GREEN + ' '.join(contact_dictionary[name].get_phones_list()) + Style.RESET_ALL
        else:
            message_to_user += Fore.WHITE + 'Phone(s): ' + Style.RESET_ALL
            message_to_user += Fore.YELLOW + 'empty' + Style.RESET_ALL

        if contact_dictionary[name].emails:
            message_to_user += Fore.WHITE + '\nEmail(s): ' + Style.RESET_ALL
            message_to_user += Fore.GREEN + f'{contact_dictionary[name].get_emails_str()}' + Style.RESET_ALL
        else:
            message_to_user += Fore.WHITE + '\nEmail(s): ' + Style.RESET_ALL
            message_to_user += Fore.YELLOW + 'empty' + Style.RESET_ALL

        if contact_dictionary[name].address:
            message_to_user += Fore.WHITE + '\nAddress: ' + Style.RESET_ALL
            message_to_user += Fore.GREEN + f'{contact_dictionary[name].address.value}' + Style.RESET_ALL
        else:
            message_to_user += Fore.WHITE + '\nAddress: ' + Style.RESET_ALL
            message_to_user += Fore.YELLOW + 'empty' + Style.RESET_ALL

        if contact_dictionary[name].birthday:
            message_to_user += Fore.WHITE + '\nBirthday: ' + Style.RESET_ALL
            if contact_dictionary[name].days_to_birthday() == 365 or contact_dictionary[name].days_to_birthday() == 366:
                message_to_user += Fore.GREEN + f'{contact_dictionary[name].birthday.value.date()} (Happy Birthday!!!)\n'\
                                + Style.RESET_ALL
            else:
                message_to_user += Fore.GREEN + f'{contact_dictionary[name].birthday.value.date()} '\
                                                f'({contact_dictionary[name].days_to_birthday()} days left until '\
                                                'the birthday)\n' + Style.RESET_ALL
        else:
            message_to_user += Fore.WHITE + '\nBirthday: ' + Style.RESET_ALL
            message_to_user += Fore.YELLOW + 'empty\n' + Style.RESET_ALL

        message_to_user += Fore.MAGENTA + '{:-^10}'.format('') + Style.RESET_ALL

        return message_to_user


class HelpOutput(OutputInterface):
    def create_output(self) -> str:
        return Fore.YELLOW + 'Descriptions:' + Style.RESET_ALL + \
                '\nc - contact, p - phone, op - old phone, b - birthday, e - email, oe - old email, a - address, n - note\n' +\
                Fore.YELLOW + '\nCommand ContactBook:\n' + Style.RESET_ALL + \
                'First command to create contact. Command "add" adds "c" and "p". Example (add c p)\n'\
                'Command "remove" delete "c". Example (remove c)\n'\
                'Command "add phone" adds "p" for "c". Example (add phone c p)\n'\
                'Command "phone" show "p" for "c". Example (phone c)\n'\
                'Command "change phone" change "op" on "p". Example (change phone c op p)\n'\
                'Command "remove phone" delete "p". Example (remove phone c p)\n'\
                'Command "add email" adds "e" for "c". Example (add email c e)\n'\
                'Command "email" show "e" for "c". Example (email c )\n'\
                'Command "change email" change "oe" on "e". Example (change email c oe e)\n'\
                'Command "remove email" delete "e". Example (remove email c e)\n'\
                'Command "add address" adds "a" for  "c". Example (add address c a)\n'\
                'Command "change address" change "a". Example (change address c a)\n'\
                'Command "remove address" delete "a". Example (remove address c)\n'\
                'Command "add birthday" adds "b" for "c". Example (add birthday c b)\n'\
                'Command "change birthday" change "b". Example (change birthday c b)\n'\
                'Command "remove birthday" delete "b". Example (remove birthday c)\n'\
                'Command "find" search information in contactbook and show match. Example (find 99) or (find aa)\n'\
                'Command "show" show all added information in "c". Example (show c)\n'\
                'Command "show all" show all contactbook. Example (show all)' +\
                Fore.YELLOW + '\nCommand NoteBook:\n' + Style.RESET_ALL + \
                'Command "add note" add note. Example (add note name text)\n'\
                'Command "change note" change note. Example (change note name text)\n'\
                'Command "remove note" delete note. Example (remove note name)\n'\
                'Command "find notes" search by text. Example (find note text)\n'\
                'Command "sort note" sort note. Example (sort note)\n'\
                'Command "show note" show note. Example (show note name)\n'\
                'Command "show notes" show all note. Example (show notes)' +\
                Fore.YELLOW + '\nCommand for sort file in folder:\n' + Style.RESET_ALL + \
                'Command "sort". Example (sort path_folder)\n'
