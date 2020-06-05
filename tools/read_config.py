import configparser
import tools.project_path as tool_path


class ReadConfig(object):

    @staticmethod
    def get_config(file_path, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]


# config_info = ReadConfig()
# config_info.get_config(tool_path.test_config_path, 'MODE', 'mode')
# print(config_info.get_config(tool_path.test_config_path, 'MODE', 'mode'))

