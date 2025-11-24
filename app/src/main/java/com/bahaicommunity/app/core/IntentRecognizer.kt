package com.bahaicommunity.app.core

/**
 * A simple, rule-based intent recognizer.
 * This will be expanded with more sophisticated NLU capabilities later.
 */
class IntentRecognizer {

    fun recognize(rawText: String): RecognizedIntent {
        val lowerCaseText = rawText.lowercase()

        // Simple keyword-based action recognition
        val action = when {
            lowerCaseText.contains("create") || lowerCaseText.contains("add") || lowerCaseText.contains("build") -> ActionType.CREATE
            lowerCaseText.contains("read") || lowerCaseText.contains("show") || lowerCaseText.contains("list") -> ActionType.READ
            lowerCaseText.contains("update") || lowerCaseText.contains("change") -> ActionType.UPDATE
            lowerCaseText.contains("delete") || lowerCaseText.contains("remove") -> ActionType.DELETE
            else -> ActionType.UNKNOWN
        }

        // Simple target extraction (very naive for now)
        val target = lowerCaseText.split(" ").lastOrNull()

        return RecognizedIntent(
            action = action,
            target = target,
            attributes = emptyMap() // Attribute extraction will be implemented later
        )
    }
}
