

import configparser


class Config:
    
    def get_config(self):
        config = configparser.ConfigParser()
        config.read("../setting/config.ini")

        # secs = config.sections()
        # options = config.options(f"{database}")
        # items = config.items(f"{database}")
        # host = config.get("mysql", "host")

        return config

    def get_parameters(self,database):

        dict = {}
        config = self.get_config()
        for item in config.options(database):
              dict[item] = config.get(database,item)

        return dict




# if __name__ == '__main__':
#     config = Config()
#     conn = config.get_config()
#     data = config.get_parameters('code')
#     print(data)
#     print(data.get('893811000945-3H'.lower()))