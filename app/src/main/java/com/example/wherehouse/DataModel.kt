package com.example.wherehouse
import com.google.gson.annotations.SerializedName

data class DataModel(
    @SerializedName("ItemID")
    val itemId: Int,

    @SerializedName("ItemName")
    val itemName: String,

    @SerializedName("ExpiryDate")
    val expiryDate: String,

    @SerializedName("Quantity")
    val quantity: Int,

    @SerializedName("Location")
    val location: String
)
