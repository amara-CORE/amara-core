#!/bin/bash

# Guardian.sh - Script to create the Guardian system structure

echo "Creating Guardian system structure..."

# Root directories
mkdir -p guardian_core
mkdir -p guardian_units
mkdir -p guardian_logs
mkdir -p guardian_storage
mkdir -p guardian_mail

# Files in guardian_core
touch guardian_core/guardian_main.sh
touch guardian_core/guardian_config.sh
touch guardian_core/guardian_constants.sh

# Files in guardian_units
touch guardian_units/check_amara_pid.sh
touch guardian_units/resource_monitor.sh
touch guardian_units/spam_detector.sh
touch guardian_units/network_guard.sh
touch guardian_units/whitelist_checker.sh

# Files in guardian_logs
touch guardian_logs/last_action.log
touch guardian_logs/resource_usage.log
touch guardian_logs/suspicious_activity.log

# Files in guardian_storage
touch guardian_storage/guard_trigger.flag
touch guardian_storage/allowed_bch.txt
touch guardian_storage/mail_template.txt

# Files in guardian_mail
touch guardian_mail/send_email.sh
touch guardian_mail/email_config.sh

echo "Guardian system structure created successfully!"