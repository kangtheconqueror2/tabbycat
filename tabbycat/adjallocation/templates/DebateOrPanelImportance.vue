<template>
  <div @mouseover="showTooltip=true" @mouseleave="showTooltip=false"
       class="flex-4 flex-truncate d-flex border-right align-items-center">

    <input max="2" min="-2" step="1" type="range" v-model="importance">

    <div class="tooltip top tooltip-vue mt-4 ml-3" role="tooltip" v-if="showTooltip">
      <div class="tooltip-arrow"></div>
      <div class="tooltip-inner">{{ importanceDescription }}</div>
    </div>

  </div>
</template>

<script>

export default {
  mixins: [],
  data: function () {
    return { showTooltip: false }
  },
  props: { debateOrPanel: Object },
  computed: {
    importanceDescription: function () {
      if (this.importance === 2) {
        return 'V.I.P.'
      } else if (this.importance === 1) {
        return 'Important'
      } else if (this.importance === 0) {
        return 'Neutral'
      } else if (this.importance === -1) {
        return 'Unimportant'
      } else if (this.importance === -2) {
        return '¯\\_(ツ)_/¯'
      }
      return null
    },
    importance: {
      get () {
        return parseInt(this.debateOrPanel.importance)
      },
      set (value) {
        // Pass a message to the parent component to then save a change to the store
        let importanceChanges = [{ 'id': this.debateOrPanel.id, 'importance': value }]
        this.$store.dispatch('updateDebatesOrPanelsAttribute', { 'importance': importanceChanges })
      },
    },
  },
}
</script>
