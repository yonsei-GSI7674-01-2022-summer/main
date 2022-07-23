sudo apt-get update && sudo apt-get install gnupg2 apt-transport-https default-jre openjdk-8-jdk nginx -y
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list


sudo apt-get update && sudo apt-get install elasticsearch
sudo service elasticsearch start
sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-nori
sudo sed -i 's/#network.host: 192.168.0.1/network.host: 0.0.0.0/g' /etc/elasticsearch/elasticsearch.yml
sudo sed -i 's/#http.port: 9200/http.port: 9000/g' /etc/elasticsearch/elasticsearch.yml
echo "transport.host: localhost" | sudo tee -a /etc/elasticsearch/elasticsearch.yml
echo "discovery.type: single-node" | sudo tee -a /etc/elasticsearch/elasticsearch.yml
sudo service elasticsearch restart

sudo apt-get install kibana -y
sudo sed -i 's/#server.port: 5601/server.port: 8500/g' /etc/kibana/kibana.yml
sudo sed -i 's/#server.host: "localhost"/server.host: "0.0.0.0"/g' /etc/kibana/kibana.yml
sudo sed -i 's&#elasticsearch.hosts: \["http://localhost:9200"]&elasticsearch.hosts: ["http://localhost:9000"]&g' /etc/kibana/kibana.yml
/etc/kibana/kibana.yml
sudo systemctl start kibana
sudo ufw allow 8500/tcp


sudo apt-get update && sudo apt-get install logstash -y
sudo chown -R logstash.logstash /usr/share/logstash
sudo chmod 777 /usr/share/logstash/data
