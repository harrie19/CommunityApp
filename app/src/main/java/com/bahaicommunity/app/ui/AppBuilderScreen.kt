package com.bahaicommunity.app.ui

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel

@Composable
fun AppBuilderScreen(viewModel: AppBuilderViewModel = viewModel()) {
    val uiState by viewModel.uiState.collectAsState()

    Surface(modifier = Modifier.fillMaxSize()) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text("App Builder Prototype")

            OutlinedTextField(
                value = uiState.appDescription,
                onValueChange = { viewModel.onDescriptionChange(it) },
                label = { Text("Enter App Description") },
                modifier = Modifier.fillMaxWidth()
            )

            Spacer(modifier = Modifier.height(16.dp))

            Button(
                onClick = { viewModel.generateCode() },
                enabled = uiState.appDescription.isNotBlank()
            ) {
                Text("Generate Code")
            }

            Spacer(modifier = Modifier.height(16.dp))

            Text("Generated Code:")
            Surface(
                modifier = Modifier.fillMaxWidth().weight(1f),
                tonalElevation = 2.dp
            ) {
                Text(
                    text = uiState.generatedCode,
                    modifier = Modifier.padding(8.dp)
                )
            }
        }
    }
}
