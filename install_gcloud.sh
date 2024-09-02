#!/bin/bash

# Set a central location for Google Cloud SDK installation
INSTALL_DIR="$HOME/tools"
GCLOUD_SDK_DIR="$INSTALL_DIR/google-cloud-sdk"
GCLOUD_BIN="$GCLOUD_SDK_DIR/bin/gcloud"

# Check if gcloud binary exists, if not, install it
[ -f "$GCLOUD_BIN" ] || {
    echo "Google Cloud SDK not found. Installing..."

    # Create the directory if it doesn't exist
    mkdir -p "$INSTALL_DIR"

    # Navigate to the central directory
    cd "$INSTALL_DIR"

    # Download Google Cloud CLI into the central directory
    curl -o "$INSTALL_DIR/google-cloud-cli-linux-x86_64.tar.gz" https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz

    # Extract the tarball in the central directory
    tar -xf "$INSTALL_DIR/google-cloud-cli-linux-x86_64.tar.gz" -C "$INSTALL_DIR"

    # Navigate to the extracted directory
    cd "$GCLOUD_SDK_DIR"

    # Run the install script with minimal setup options
    ./install.sh --quiet --path-update true --command-completion true

    # Clean up the tarball after extraction
    rm "$INSTALL_DIR/google-cloud-cli-linux-x86_64.tar.gz"

    echo "Google Cloud SDK installation completed."
}

# Check if the path.bash.inc file exists and source it if available
[ -f "$GCLOUD_SDK_DIR/path.bash.inc" ] && source "$GCLOUD_SDK_DIR/path.bash.inc"

echo "Setup complete."
