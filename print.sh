AndroidManifest.xml:

<manifest xmlns:android="http://schemas.android.com/apk/res/android"    package="com.example.ransomware">
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <application
        android:name=".RansomwareApp"        android:allowBackup="false"
        android:icon="@mipmap/ic_launcher"        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        <activity android:name=".MainActivity">            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />            </intent-filter>
        </activity>
        <activity android:name=".RansomActivity" />
        <service android:name=".RansomwareService" />
        <receiver android:name=".BootReceiver"            android:enabled="true"
            android:exported="true">            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED" />            </intent-filter>
        </receiver>
    </application>
</manifest>