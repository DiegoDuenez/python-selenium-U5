from app.Interface import Interface
from selenium.webdriver.common.keys import Keys
from app.Config import Config


path_config = "config.json"
config = Config(path_config).load()


interface = Interface(config['driver'], config['site'])
interface.open()
  
for e in config['elements']:
    interface.sleep(e['timesleep']).web().element(e['event'], e['by'], e['selector'], e['value'])


