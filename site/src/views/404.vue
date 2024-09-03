<template>
    <div>404</div>
</template>

<script lang='ts'>
export default {
    setup() {
        return {}
    },
    beforeCreate() {
        location.href = '/'
    }
}
</script>

<style lang='scss' scoped>

</style>
