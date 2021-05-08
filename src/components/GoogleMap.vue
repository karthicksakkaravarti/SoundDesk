<template>
  <vl-map data-projection="EPSG:4326" style="height: 400px">
    <vl-view
      :zoom.sync="zoom"
      :center.sync="center"
      :rotation.sync="rotation"
    ></vl-view>

    <vl-layer-tile>
      <vl-source-osm></vl-source-osm>
    </vl-layer-tile>

    <!-- interactions -->
    <vl-interaction-select :features.sync="selectedFeatures">
      <template slot-scope="select">
        <!-- selected feature popup -->
        <vl-overlay
          class="feature-popup"
          v-for="feature in select.features"
          :key="feature.id"
          :id="feature.id"
          :position="pointOnSurface(feature.geometry)"
          :auto-pan="true"
          :auto-pan-animation="{ duration: 300 }"
        >
          <template slot-scope="">
            <section class="card">
              <v-card>
                <v-card-title>
                  VMD Name: {{ feature.properties.i.VMDName }}
                  <a
                    class="card-header-icon"
                    title="Close"
                    @click="
                      selectedFeatures = selectedFeatures.filter(
                        (f) => f.id !== feature.id
                      )
                    "
                  >
                    <v-icon color="red"> mdi-close </v-icon>
                  </a>
                </v-card-title>
                <v-divider></v-divider>
                <v-card-text>
                  <header class="card-header"></header>
                  <div>
                    <div>
                      <ul>
                        <li>
                          VMD Location : {{ feature.properties.i.VMDLocation }}
                        </li>
                        <li>
                          VMD Latitude : {{ feature.properties.i.VMDLatitude }}
                        </li>
                        <li>
                          VMD Longitude :
                          {{ feature.properties.i.VMDLongitude }}
                        </li>
                        <li>
                          VMD IPAddress :
                          {{ feature.properties.i.VMDIPAddress }}
                        </li>
                        <li>
                          VMD Height:
                          {{ feature.properties.i.VMDResolutionHeight }}
                        </li>
                        <li>
                          VMD width :
                          {{ feature.properties.i.VMDResolutionwidth }}
                        </li>
                        <li>
                          VMD Status: {{ feature.properties.i.VMDStatus }}
                        </li>
                      </ul>
                    </div>
                  </div>
                </v-card-text>
              </v-card>
            </section>
          </template>
        </vl-overlay>
        <!--// selected popup -->
      </template>
    </vl-interaction-select>
    <!--// interactions -->

    <vl-feature
      v-for="i in vmd"
      v-bind:key="i.id"
      :id="i.id"
      :ref="i.id"
      :properties="{ i }"
    >
      <template slot-scope="">
        <vl-geom-point
          :coordinates="[Number(i.VMDLatitude), Number(i.VMDLongitude)]"
        />
        <vl-style-box>
          <vl-style-icon
            :src="
              i.VMDStatus == 'Active'
                ? 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png'
                : 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png'
            "
            :scale="0.5"
            :anchor="[0.1, 0.95]"
            :size="[128, 128]"
          >
            <v-icon>mdi-map-marker</v-icon></vl-style-icon
          >
        </vl-style-box>
      </template>
    </vl-feature>
  </vl-map>
</template>

<script>
import { findPointOnSurface } from "vuelayers/lib/ol-ext";

export default {
  data() {
    return {
      selectedFeatures: [],
      zoom: 2,
      center: [83.1992864473144, 20.405348857423434],
      rotation: 0,
    };
  },
  methods: {
    pointOnSurface: findPointOnSurface,
  },
  props: {
    vmd: {},
  },
};
</script>

<style lang="sass" >
@import ~bulma/sass/utilities/_all
html, body, #app
    width: 100%
    height: 100%
    margin: 0
    padding: 0
.vld-demo-app
    position: relative
    .map
        height: 100%
        width: 100%
    .map-panel
        padding: 0
    .panel-heading
        box-shadow: 0 .25em .5em transparentize($dark, 0.8)
    .panel-content
        background: $white
        box-shadow: 0 .25em .5em transparentize($dark, 0.8)
    .panel-block
        &.draw-panel
        .buttons
            .button
                display: block
                flex: 1 1 100%
    +tablet()
        position: absolute
        top: 0
        right: 0
        max-height: 500px
        width: 22em
    .base-layers-panel
        position: absolute
        left: 50%
        bottom: 20px
        transform: translateX(-50%)
    .feature-popup
        position: absolute
        left: -50px
        bottom: 12px
        width: 20em
        max-width: none
    &:after, &:before
        top: 100%
        border: solid transparent
        content: ' '
        height: 0
        width: 0
        position: absolute
        pointer-events: none
    &:after
        border-top-color: white
        border-width: 10px
        left: 48px
        margin-left: -10px
    &:before
        border-top-color: #cccccc
        border-width: 11px
        left: 48px
        margin-left: -11px
    .card-content
        max-height: 20em
        overflow: auto
    .content
        word-break: break-all
</style>