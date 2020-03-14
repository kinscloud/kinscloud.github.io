cat > /etc/docker/daemon.json << EOF
{
  "registry-mirrors": ["https://tnxkcso1.mirror.aliyuncs.com"]
}
EOF
systemctl restart docker