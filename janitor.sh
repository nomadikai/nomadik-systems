#!/bin/bash
# Nomadik Systems: Weekly Maintenance
echo "[*] Cleaning package cache..."
sudo apt-get clean
echo "[*] Removing old dependencies..."
sudo apt-get autoremove -y
echo "[*] Clearing user thumbnail and pip caches..."
rm -rf ~/.cache/thumbnails/*
rm -rf ~/.cache/pip/*
echo "[*] Current Disk Usage:"
df -h /
