sudo certbot certonly --nginx --dry-run -d skae.in -d www.skae.in


certbot -d skae.in,www.skae.in,test.skae.in --force-renewal

sudo systemctl daemon-reload
sudo systemctl restart gunicorn

sudo nginx -t && sudo systemctl restart nginx



some additional commands
$ sudo ufw enable
sudo ufw allow ssh
sudo ufw enable


chmod o+rx /example_root_folder #to give folder permission
sudo service nginx stop
sudo service nginx start

sudo certbot -v
