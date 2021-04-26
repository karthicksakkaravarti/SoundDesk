import { router } from '../router/index';

export const utility = {
    methods:{
        routing(route){
            if (route == 'dashboard'){
                router.push('/dashboard')
            }
            else if (route == 'Usermanagement'){
                router.push('/Usermanagement')
            }
            else if (route == 'VmdManagement'){
                router.push('/VmdManagement')
            }
            else if (route == 'VmdConfiguration'){
                router.push('/VmdConfiguration')
            }
            else if (route == 'SendMessage'){
                router.push('/SendMessage')
            }
            else if (route == 'MessagingConfig'){
                router.push('/MessagingConfig')
            }
            else if (route == 'predefined'){
                router.push('/Predefined')
            }
        }
    }
}
