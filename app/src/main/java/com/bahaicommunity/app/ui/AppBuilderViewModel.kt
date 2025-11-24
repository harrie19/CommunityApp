package com.bahaicommunity.app.ui

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update

data class AppBuilderUiState(
    val appDescription: String = "",
    val generatedCode: String = ""
)

class AppBuilderViewModel : ViewModel() {

    private val _uiState = MutableStateFlow(AppBuilderUiState())
    val uiState: StateFlow<AppBuilderUiState> = _uiState.asStateFlow()

    fun onDescriptionChange(newDescription: String) {
        _uiState.update { it.copy(appDescription = newDescription) }
    }

    fun generateCode() {
        val description = _uiState.value.appDescription
        if (description.isBlank()) return

        // This will be replaced with Ollama integration
        val generatedCode = """
            // Generated code for: $description
            
            class GeneratedApp {
                // Your app logic here based on: $description
            }
        """.trimIndent()

        _uiState.update { it.copy(generatedCode = generatedCode) }
    }
}
