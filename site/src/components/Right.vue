<script setup lang="ts">
import ChangeLog from './ChangeLog.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
</script>

<template>
  <ChangeLog>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template>ChangeLog</template>
  </ChangeLog>


</template>
