# Set the application name and package name
APP_NAME := myapp
APP_PACKAGE := com.example.ransomware

# Set the Java Development Kit (JDK) path
JAVA_HOME := /usr

# Set the Android SDK path
ANDROID_SDK_ROOT := /usr/lib/android-sdk

# Set the Android API level
ANDROID_API := 21
ANDROID_TOOLCHAIN_VERSION := 28.0.3

# Define the all target
all: app-release.apk

# Define the clean target
.PHONY: clean
clean:
    rm -rf build

# Define the app-release.apk target
app-release.apk:
    @mkdir -p app/build/intermediates/classes/release/
    @mkdir -p app/build/intermediates/bundles/release/
    @"$(JAVA_HOME)/bin/javac" -d app/build/intermediates/classes/release \
    -classpath "$(ANDROID_SDK_ROOT)/platforms/android-$(ANDROID_API)/android.jar":\
    app/build/intermediates/classes/debug \
    app/src/main/java/**/*.java \
    && "$(JAVA_HOME)/bin/dx" --dex \
    --output=app/build/intermediates/bundles/release/ \
    app/build/intermediates/classes/release \
    && "$(ANDROID_SDK_ROOT)/build-tools/$(ANDROID_TOOLCHAIN_VERSION)/aapt" \
    package \
    -f \
    -M app/app/src/main/AndroidManifest.xml \
    -S app/app/src/main/res \
    -I "$(ANDROID_SDK_ROOT)/platforms/android-$(ANDROID_API)/android.jar" \
    -F app/build/outputs/apk/app-release.apk \
    -m \
    && "$(JAVA_HOME)/bin/zipalign" \
    -v 4 \
    app/build/outputs/apk/app-release.apk \
    app/build/outputs/apk/app-release-aligned.apk