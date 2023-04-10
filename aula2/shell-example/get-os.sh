#!/bin/bash

# Info do SO 
os_name=$(uname -s)
os_version=$(uname -r)

# pega informacoes sobre o CPU
cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}')

# pega informacoes sobre RAM 
ram_total=$(free -m | grep Mem | awk '{print $2}')
ram_used=$(free -m | grep Mem | awk '{print $3}')
ram_usage=$((ram_used * 100 / ram_total))

# pega informacoes de uso do storage 
storage_total=$(df -h / | awk '{print $2}' | tail -1)
storage_used=$(df -h / | awk '{print $3}' | tail -1)
storage_usage=$(df -h / | awk '{print $5}' | tail -1)

# imprimi uma tabela no console com as informacoes
printf "| %-20s | %-20s |\n" "OS Name" "$os_name"
printf "| %-20s | %-20s |\n" "OS Version" "$os_version"
printf "| %-20s | %-20s |\n" "USO CPU" "$cpu_usage"
printf "| %-20s | %-20s |\n" "USO RAM" "$ram_usage%"
printf "| %-20s | %-20s |\n" "USO Storage" "$storage_usage de $storage_total"
