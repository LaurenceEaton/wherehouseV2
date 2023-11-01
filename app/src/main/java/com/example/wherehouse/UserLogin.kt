package com.example.wherehouse

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.annotation.Nullable
import androidx.appcompat.app.AppCompatActivity
import com.google.zxing.integration.android.IntentIntegrator
import com.google.zxing.integration.android.IntentResult

class UserLogin : AppCompatActivity() {

    companion object {
        private const val BARCODE_SCAN_REQUEST = 1
    }

    private lateinit var barcodeEditText: EditText

    private fun openNextPage() {
        val intent = Intent(this, MainMenu::class.java)
        startActivity(intent)
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.user_login)

        val cameraButton: Button = findViewById(R.id.cameraButton)
        barcodeEditText = findViewById(R.id.barcodeEditText)

        cameraButton.setOnClickListener {
            val integrator = IntentIntegrator(this@UserLogin)
            integrator.setDesiredBarcodeFormats(listOf(IntentIntegrator.CODE_39))
            integrator.setPrompt("Scan a barcode")
            integrator.setCameraId(0)
            integrator.setBeepEnabled(false)
            integrator.setBarcodeImageEnabled(true)
            integrator.initiateScan()
        }

        val submitButton: Button = findViewById(R.id.submitButton)
        submitButton.setOnClickListener {
            val userInput = barcodeEditText.text.toString()
            if (userInput == "12345678") {
                openNextPage()
            }
        }
    }



    override fun onActivityResult(requestCode: Int, resultCode: Int, @Nullable data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        val result: IntentResult? = IntentIntegrator.parseActivityResult(requestCode, resultCode, data)

        if (result != null && result.contents != null) {
            val scannedBarcode = result.contents
            if ("12345678" == scannedBarcode) {
                openNextPage()
            }
        }
    }

}
