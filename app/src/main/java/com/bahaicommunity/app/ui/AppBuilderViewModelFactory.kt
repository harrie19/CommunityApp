package com.bahaicommunity.app.ui

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.bahaicommunity.app.data.AuditRepository

/**
 * Factory for creating a AppBuilderViewModel with a constructor that takes a repository.
 */
class AppBuilderViewModelFactory(private val repository: AuditRepository) : ViewModelProvider.Factory {
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        if (modelClass.isAssignableFrom(AppBuilderViewModel::class.java)) {
            @Suppress("UNCHECKED_CAST")
            return AppBuilderViewModel(repository) as T
        }
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}
