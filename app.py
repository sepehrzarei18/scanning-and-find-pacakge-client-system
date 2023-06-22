import os
import itertools

class Extensions : 
    @staticmethod
    def replaceEmptyString (arg) : 
        new_string = ""
        is_whitespace = False
        for char in arg:
            if char.isspace() or not char:
                if not is_whitespace:
                    new_string += char
                    is_whitespace = True
            else:
                new_string += char
                is_whitespace = False
        return new_string    

class PacakgeService : 

    def ComparePackages (self) : 
        commandList = os.popen('pip list', 'r').read().split("\n")
        system_packages = self.__fixed_name_of_packages(itertools.islice(commandList, 2 , None))
        
        requirements_packages = []
        file_location = f'{os.getcwd()}/requirements.txt'
        
        try : 
            with open (file_location, 'r') as file : 
                for line in file.readlines(): 
                    if line == " " :
                        continue
                    requirements_packages.append(line)
                requirements_packages = self.__fixed_name_of_packages(requirements_packages)

                packages_should_install_count = 0 

                for package in requirements_packages : 
                    if package not in system_packages : 
                        print (f'install ({package}) package')
                        packages_should_install_count += 1

                print (f'scannig is done ! you have to install {packages_should_install_count} packages')

        except FileNotFoundError : 
            print ('requirements file dosent exists !')


    def __fixed_name_of_packages (self ,list_arg : list) : 

        return_list = []

        for item in list_arg : 
            text = Extensions.replaceEmptyString(item)
            items = None

            try : 
                items = text.split(" ")

                if len(items) == 2 :
                    return_list.append({'version' : items[1] , 'packages' : items[0]})
            except : 
                pass

        return return_list
        

def main () :
    service = PacakgeService()
    service.ComparePackages()


if __name__ == '__main__': 
    main () 