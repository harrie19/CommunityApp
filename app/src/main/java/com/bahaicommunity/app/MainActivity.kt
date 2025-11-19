package com.example.appbuilder

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView

class MainActivity : AppCompatActivity() {

    private lateinit var appDescriptionInput: EditText
    private lateinit var generateButton: Button
    private lateinit var codeOutputText: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        initializeViews()
        setupGenerateButton()
    }

    private fun initializeViews() {
        appDescriptionInput = findViewById(R.id.appDescriptionInput)
        generateButton = findViewById(R.id.generateButton)
        codeOutputText = findViewById(R.id.codeOutputText)
    }

    private fun setupGenerateButton() {
        generateButton.setOnClickListener {
            val appDescription = appDescriptionInput.text.toString()
            if (appDescription.isNotEmpty()) {
                codeOutputText.text = "Generating code for: $appDescription\n\n"
                generateAppCode(appDescription)
            } else {
                codeOutputText.text = "Please enter an app description"
            }
        }
    }

    private fun generateAppCode(description: String) {
        // This will be replaced with Ollama integration
        val generatedCode = """
            // Generated code for: $description
            
            class GeneratedApp : AppCompatActivity() {
                override fun onCreate(savedInstanceState: Bundle?) {
                    super.onCreate(savedInstanceState)
                    setContentView(R.layout.activity_generated)
                    
                    // Your app logic here based on: $description
                }
            }
        """.trimIndent()

        codeOutputText.append(generatedCode)
    }
}