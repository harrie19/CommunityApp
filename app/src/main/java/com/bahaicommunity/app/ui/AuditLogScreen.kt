package com.bahaicommunity.app.ui

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Card
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.bahaicommunity.app.data.AuditRecord

@Composable
fun AuditLogScreen(records: List<AuditRecord>) {
    LazyColumn(
        contentPadding = PaddingValues(16.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        items(records) { record ->
            AuditRecordCard(record = record)
        }
    }
}

@Composable
private fun AuditRecordCard(record: AuditRecord) {
    Card(modifier = Modifier.fillMaxWidth()) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text("Action: ${record.action}", fontWeight = FontWeight.Bold)
            Text("Actor: ${record.actor}")
            Text("Timestamp: ${record.timestamp}")
            Text("Input: ${record.inputSummary}")
        }
    }
}
