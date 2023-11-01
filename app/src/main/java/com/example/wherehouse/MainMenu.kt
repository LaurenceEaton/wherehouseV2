package com.example.wherehouse

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class MainMenu : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main_menu)
    }

    fun openviewStockActivity(view: View) {
        val intent = Intent(this, ViewStock::class.java)
        startActivity(intent)
    }

    fun openeditStockActivity(view: View) {
        val intent = Intent(this, EditStock::class.java)
        startActivity(intent)
    }
    fun openitemWithdrawalsActivity(view: View) {
        val intent = Intent(this, ItemWithdrawals::class.java)
        startActivity(intent)
    }
    fun openitemDepositsActivity(view: View) {
        val intent = Intent(this, ItemDeposits::class.java)
        startActivity(intent)
    }
    fun opencycleCountingActivity(view: View) {
        val intent = Intent(this, CycleCounting::class.java)
        startActivity(intent)
    }
    fun openaddNewItemTypeToStockActivity(view: View) {
        val intent = Intent(this, AddNewItemTypeToStock::class.java)
        startActivity(intent)
    }
    fun openstockPredictionActivity(view: View) {
        val intent = Intent(this, StockPrediction::class.java)
        startActivity(intent)
    }



}
