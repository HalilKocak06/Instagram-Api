from instagrapi import Client
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='172.16.231.160:9092')

cl = Client()
cl.login("zamazingo091","BenBurdayim132")


threads = cl.direct_threads()
for th in threads:
  for m in th.messages:
     producer.send('instagram', m.text.encode('UTF-8'))
     producer.flush()
     