package com.bahaicommunity.app

import android.app.Application
import com.bahaicommunity.app.data.AppDatabase

/**
 * Application class to hold the singleton instance of the database.
 */
class CodeCellApplication : Application() {
    val database: AppDatabase by lazy { AppDatabase.getDatabase(this) }
}
