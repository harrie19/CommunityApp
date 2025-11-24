package com.bahaicommunity.app.data

import androidx.room.Entity
import androidx.room.PrimaryKey

/**
 * Represents a single, immutable audit record in the Flight Recorder.
 * This corresponds to the AuditRecord schema in the master plan.
 */
@Entity(tableName = "audit_records")
data class AuditRecord(
    @PrimaryKey(autoGenerate = true)
    val id: Long = 0,
    val timestamp: String,
    val actor: String,
    val action: String,
    val inputSummary: String,
    // Note: Storing lists of complex objects requires TypeConverters in Room.
    // For now, we'll store them as plain text and parse them later.
    val proposedChanges: String, // e.g., JSON string
    val testResults: String, // e.g., JSON string
    val hash: String,
    val signature: String
)
