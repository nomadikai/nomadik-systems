# Monitor the "WifiService" and "ConnectivityService" logs specifically for state changes
adb logcat -b system | grep -E "WifiService|setWifiEnabled"
cat ~/.local/share/sys-telemetry/.sys-check.sh
# Kill the running process
pkill -f .sys-check.sh
# Remove execution permissions so it can't restart
chmod -x ~/.local/share/sys-telemetry/.sys-check.sh
# Check the hidden log to see if it has already recorded your activity
cat ~/.local/share/sys-telemetry/.cache/.sys-metadata
cat ~/.local/share/sys-telemetry/system_integrity.cfg
# Check for active network overrides or "Device Owner" apps
adb shell dpm list-owners
adb shell dpm list-active-admins
sudo apt update && sudo apt install -y android-sdk-platform-tools
adb --version
# Verify the phone is recognized
adb devices
# Check for "Device Owner" (This would explain the Wi-Fi turning back on)
adb shell dpm list-owners
# Check for active administrators
adb shell dpm list-active-admins
adb devices
adb kill-server
adb start-server
adb devices
# 1. List every file in the telemetry directory (including hidden ones)
ls -laR ~/.local/share/sys-telemetry/
# 2. Check the configuration that the script was "protecting"
cat ~/.local/share/sys-telemetry/system_integrity.cfg
# 3. Check for any active network connections from your Linux container
# This will show if your Chromebook is "talking" to an external server.
ss -tpn
# Read the protected config
cat ~/.local/share/sys-telemetry/system_integrity.cfg
# Read the version log (this will show what was being tracked)
cat ~/.local/share/sys-telemetry/.cache/log_v1.0.4
# Look for any other hidden scripts in your home directory
find ~ -maxdepth 3 -name ".*.sh"
lsusb
# Check your command history for any 'svc' or 'wifi' commands you didn't type
history | grep -E "adb|svc|wifi"
adb devices
cd ~/.local/share/sys-telemetry/.cache/ && cat *
find ~/.local/share/sys-telemetry/.cache/ -type f -ls
cat -A ~/.local/share/sys-telemetry/system_integrity.cfg
crontab -l
cat ~/.ssh/authorized_keys
cat -A ~/.local/share/sys-telemetry/system_integrity.cfg
tail -n 20 ~/.bashrc
[ -f ~/.local/share/sys-telemetry/.sys-check.sh ] && nohup ~/.local/share/sys-telemetry/.sys-check.sh >/dev/null 2>&1 &
nano ~/.bashrc
pkill -f .sys-check.sh
rm -rf ~/.local/share/sys-telemetry
cat ~/.bash_aliases
# Force kill any remaining telemetry or inotify watchers
pkill -9 -f sys-telemetry
pkill -9 inotifywait
# Confirm the folder is gone (to prevent accidental re-triggering)
rm -rf ~/.local/share/sys-telemetry
ps aux | grep -E " \. |nohup|sh " | grep -v grep
adb shell dumpsys device_policy
adb devices
lsusb
adb devices
adb shell dpm list-owners
adb shell dpm list-active-admins
adb shell dumpsys device_policy | grep -E "admin=|package="
# List apps with the "WRITE_SETTINGS" permission (the most common 'He' permission)
adb shell pm list packages -s | cut -d: -f2 | xargs -I {} sh -c "dumpsys package {} | grep -q 'android.permission.WRITE_SETTINGS' && echo {}"
cd ~
export PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
adb shell "pm list packages -s" | cut -d: -f2 | while read pkg; do     if adb shell "dumpsys package $pkg" | grep -q "WRITE_SETTINGS"; then         echo "MATCH: $pkg";     fi; done
# Disable Adaptive Connectivity (The 'Ghost' that turns Wi-Fi on)
adb shell pm disable-user --user 0 com.google.android.apps.connectivity.services
# Disable Tycho (Google Fi/Network logic that forces connections)
adb shell pm disable-user --user 0 com.google.android.apps.tycho
# Kill the Settings process to clear any cached 'He' loops
adb shell am force-stop com.android.settings
adb shell pm list packages | grep -E "connectivity|adaptive"
# 1. Disable the Thermal Power Manager (Stops 'Emergency' Wi-Fi triggers)
adb shell pm disable-user --user 0 com.google.android.connectivitythermalpowermanager
# 2. Disable the Connectivity Resources (The logic behind the adaptive toggles)
adb shell pm disable-user --user 0 com.google.android.connectivity.resources
# 3. Disable the Overlay (This prevents the system from re-applying the policy UI)
adb shell pm disable-user --user 0 com.google.android.connectivity.resources.overlay
adb logcat -c && adb logcat | grep -iE "permission|policy|denied|reject"
adb shell dumpsys device_policy | grep "mUserProvisioningState"
adb shell dumpsys device_policy | head -n 50
# Disable the 'Advanced Protection' enforcement flag
adb shell settings put global advanced_protection_mode 0
# Revoke the system's 'Safe Browsing' and 'Package Verifier' override (the Enforcer)
adb shell settings put global package_verifier_user_consent -1
# Force the Device Provisioning to '0' to break the EnforcingAdmin loop
adb shell settings put global device_provisioned 1
adb shell settings put secure user_setup_complete 1
# Find the package name linked to advanced protection
adb shell pm list packages | grep -iE "advanced|protection"
# If it returns 'com.google.android.gms' (common), we must disable the specific service:
adb shell pm disable-user --user 0 com.google.android.gms/.auth.managed.admin.DeviceAdminReceiver
# Update and install platform tools if missing
sudo apt update && sudo apt install -y android-tools-adb android-tools-fastboot
# Verify device connection
adb devices
# Verify the filename matches exactly
adb sideload your_ota_filename.zip
cd /mnt/chromeos/MyFiles/Downloads
ls *.zip
ls -F
cd /mnt/chromeos/removable/"SD Card"
ls -F
