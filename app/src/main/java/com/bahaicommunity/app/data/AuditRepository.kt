package com.bahaicommunity.app.data

import kotlinx.coroutines.flow.Flow

/**
 * Repository that provides a single source of truth for Audit data.
 * It abstracts the data source (local database) from the rest of the app.
 */
class AuditRepository(private val auditDao: AuditDao) {

    /**
     * A flow that emits the complete list of audit records whenever the data changes.
     */
    val allAuditRecords: Flow<List<AuditRecord>> = auditDao.getAll()

    /**
     * Inserts a new audit record into the database.
     */
    suspend fun insertRecord(auditRecord: AuditRecord) {
        auditDao.insert(auditRecord)
    }
}
