anim/matrix_animation_0.xml:

<set xmlns:android="http://schemas.android.com/apk/res/android"    android:interpolator="@android:anim/linear_interpolator">
    <translate
        android:fromXDelta="100%"        android:toXDelta="0%"
        android:duration="500" />
</set>

anim/matrix_animation_1.xml:

<set xmlns:android="http://schemas.android.com/apk/res/android"    android:interpolator="@android:anim/linear_interpolator">
    <translate
        android:fromYDelta="100%"        android:toYDelta="0%"
        android:duration="500" />
</set>

anim/matrix_animation_2.xml:

<set xmlns:android="http://schemas.android.com/apk/res/android"    android:interpolator="@android:anim/linear_interpolator">
    <scale
        android:fromXScale="0%"        android:toXScale="100%"
        android:fromYScale="0%"        android:toYScale="100%"
        android:duration="500" />
</set>

anim/matrix_animation_3.xml:

<set xmlns:android="http://schemas.android.com/apk/res/android"    android:interpolator="@android:anim/linear_interpolator">
    <alpha
        android:fromAlpha="0.0"        android:toAlpha="1.0"
        android:duration="500" />
</set>

anim/matrix_animation_4.xml:

<set xmlns:android="http://schemas.android.com/apk/res/android"    android:interpolator="@android:anim/linear_interpolator">
    <translate
        android:fromXDelta="0%"        android:toXDelta="-100%"
        android:duration="500" />
</set>

anim/matrix_animation_5.xml:

<set xmlns:android="http://schemas.android.com/apk/res/android"    android:interpolator="@android:anim/linear_interpolator">
    <translate
        android:fromYDelta="0%"        android:toYDelta="-100%"
        android:duration="500" />
</set>

drawable/matrix_background_base.xml:

<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item        android:id="@+id/layer_background"
        android:drawable="@android:color/black" />
</layer-list>

mipmap-anydpi-v26/matrix_digit_57.png: (file image)
layout/activity_main.xml:

<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"    android:layout_width="match_parent"
    android:layout_height="match_parent">
</FrameLayout>

layout/activity_ransom.xml:

<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"    android:layout_width="match_parent"
    android:layout_height="match_parent">
    <RelativeLayout        android:id="@+id/layer_background"
        android:layout_width="match_parent"        android:layout_height="match_parent">
        <ImageView
            android:id="@+id/imageView_digit_57"            android:layout_width="wrap_content"
            android:layout_height="wrap_content"            android:layout_centerHorizontal="true"
            android:layout_centerVertical="true"            android:src="@mipmap/matrix_digit_57" />
    </RelativeLayout>
    <TextView
        android:id="@+id/messageTextView"        android:layout_width="wrap_content"
        android:layout_height="wrap_content"        android:layout_centerInParent="true"
        android:textColor="@color/white"        android:textSize="24sp" />
    <Button
        android:id="@+id/payButton"        android:layout_width="wrap_content"
        android:layout_height="wrap_content"        android:layout_alignParentBottom="true"
        android:layout_centerHorizontal="true"        android:layout_marginBottom="16dp"
        android:background="@color/colorAccent"        android:text="Pay $500 in Bitcoin"
        android:textColor="@color/white" />
</RelativeLayout>

values/colors.xml:

<resources>    <color name="colorPrimary">#3F51B5</color>
    <color name="colorPrimaryDark">#303F9F</color>    <color name="colorAccent">#FF4081</color>
    <color name="white">#FFFFFF</color></resources>
    
    values/strings.xml:

<resources>    <string name="app_name">Ransomware</string>
</resources>

values/styles.xml:

<resources>    <style name="AppTheme" parent="Theme.AppCompat.Light.NoActionBar">
    </style></resources>
    
    xml/matrix_background.xml:

<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item        android:id="@+id/layer_background"
        android:drawable="@android:color/black" />
</layer-list>

build.gradle:

apply plugin: 'com.android.application'
android {    compileSdkVersion 28
    defaultConfig {        applicationId "com.example.ransomware"
        minSdkVersion 21        targetSdkVersion 28
        versionCode 1        versionName "1.0"
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"    }
    buildTypes {        release {
            minifyEnabled false            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }    }
}
dependencies {    implementation fileTree(dir: 'libs', include: ['*.jar'])
    implementation 'com.android.support:appcompat-v7:28.0.0'    implementation 'com.android.support.constraint:constraint-layout:1.1.3'
    testImplementation 'junit:junit:4.12'    androidTestImplementation 'com.android.support.test:runner:1.0.2'
    androidTestImplementation 'com.android.support.test.espresso:espresso-core:3.0.2'}
    
    settings.gradle:

include ':app'