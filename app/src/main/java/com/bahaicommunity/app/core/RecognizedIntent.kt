package com.bahaicommunity.app.core

/**
 * A structured representation of the user's intent, extracted from raw text.
 */
data class RecognizedIntent(
    val action: ActionType,
    val target: String?,
    val attributes: Map<String, String>
)

enum class ActionType {
    CREATE, READ, UPDATE, DELETE, UNKNOWN
}
