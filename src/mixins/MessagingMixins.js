import {   mapActions} from 'vuex'


export const MessagingMixins = {
    computed:{

    },
    methods:{
        ...mapActions('Messaging', ['get_TextMessage', 'post_TextMessage', 'patch_TextMessage', 'delete_TextMessage',
    'get_RegionDimensionAndCoOrdinates', 'post_RegionDimensionAndCoOrdinates', 'patch_RegionDimensionAndCoOrdinates', 
'get_Schedule', 'post_Schedule', 'patch_Schedule', 'get_PublishManagement','post_PublishManagement', 'patch_PublishManagement', 'delete_PublishManagement',
'get_Playlist', 'post_Playlist', 'patch_Playlist', 'delete_Playlist']),

    }
}
