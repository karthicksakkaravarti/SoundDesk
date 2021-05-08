<template>
  <vl-map data-projection="EPSG:4326" style="height: 400px">
    <vl-view :zoom.sync="zoom" :center.sync="center" :rotation.sync="rotation"></vl-view>

    <vl-layer-tile>
      <vl-source-osm></vl-source-osm>
    </vl-layer-tile>


    <vl-feature
      id="marker"
      ref="marker"
      :properties="{ start: Date.now(), duration: 2500 }">
      <template slot-scope="">
        <vl-geom-point :coordinates="[76.991592, 10.997455]"/>
        <vl-style-box>
          <vl-style-icon
            src="https://unpkg.com/leaflet@1.3.3/dist/images/marker-icon-2x.png"
            :scale="0.5"
            :anchor="[0.1, 0.95]"
            :size="[128, 128]"/>
        </vl-style-box>

        <vl-overlay
          v-for="feature in features"
          :key="feature.id"
          :id="feature.id"
          class="feature-popup"
          :position="pointOnSurface(feature.geometry)"
          :auto-pan="true"
          :auto-pan-animation="{ duration: 300 }">
          <template slot-scope="popup">
            <section class="card">
              <header class="card-header">
                <p class="card-header-title">
                  Feature ID {{ feature.id }}
                </p>
                <a class="card-header-icon" title="Close"
                   @click="selectedFeatures = selectedFeatures.filter(f => f.id !== feature.id)">
                  <b-icon icon="close"></b-icon>
                </a>
              </header>
              <div class="card-content">
                <div class="content">
                  <p>
                    Overlay popup content for Feature with ID <strong>{{ feature.properties }}</strong>
                  </p>
                  <p>
                    Popup: {{ JSON.stringify(popup) }}
                  </p>
                  <p>
                    Feature: {{ JSON.stringify({ id: feature.id, properties: feature.properties }) }}
                  </p>
                </div>
              </div>
            </section>
          </template>
        </vl-overlay>

        <!-- <vl-overlay
          :position="[76.991592, 10.997455]"
          :offset="[10, 10]">
          <p class="is-light box content">
            Always opened overlay for Feature ID 
          </p>
        </vl-overlay> -->
      </template>
    </vl-feature>

    
  </vl-map>
</template>

<script>
import {findPointOnSurface} from 'vuelayers/lib/ol-ext'

  export default {
    data () {
      return {
        zoom: 4,
        center: [ 83.1992864473144, 20.405348857423434 ],
        rotation: 0,
      }
    },
    methods: {
        pointOnSurface: findPointOnSurface
    }
  }
</script>

<style lang="scss" scoped>
@import "~bulma/sass/utilities/all";
.map {
  position: relative;
  width: 100%;
  height: 100%;
}
.map-panel {
  padding: 0;
  .panel-heading {
    box-shadow: 0 .25em .5em transparentize($dark, 0.8);
  }
  .panel-content {
    background: $white;
    box-shadow: 0 .25em .5em transparentize($dark, 0.8);
  }
  .panel-block {
    &.draw-panel {
      .buttons {
        .button {
          display: block;
          flex: 1 1 100%;
        }
      }
    }
  }
  @include tablet() {
    position: absolute;
    top: 0;
    right: 0;
    max-height: 500px;
    width: 22em;
  }
}
.base-layers-panel {
  position: absolute;
  left: 50%;
  bottom: 20px;
  transform: translateX(-50%);
}
.feature-popup {
  position: absolute;
  left: -50px;
  bottom: 12px;
  width: 20em;
  max-width: none;
  &:after, &:before {
    top: 100%;
    border: solid transparent;
    content: ' ';
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
  }
  &:after {
    border-top-color: white;
    border-width: 10px;
    left: 48px;
    margin-left: -10px;
  }
  &:before {
    border-top-color: #cccccc;
    border-width: 11px;
    left: 48px;
    margin-left: -11px;
  }
  .card-content {
    max-height: 20em;
    overflow: auto;
  }
  .content {
    word-break: break-all;
  }
}
</style>