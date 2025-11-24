package com.bahaicommunity.app.data

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import kotlinx.coroutines.flow.Flow

/**
 * Data Access Object for the AuditRecord entity.
 */
@Dao
interface AuditDao {

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(auditRecord: AuditRecord)

    @Query("SELECT * FROM audit_records ORDER BY timestamp DESC")
    fun getAll(): Flow<List<AuditRecord>>
}
