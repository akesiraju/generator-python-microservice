docs = {
    'health_check': {
        'get': {
            'description': 'Returns the status of <%= APP_NAME %>.',
            'responses': {
                '200': {
                    'description': '<%= APP_NAME %> is up and running.'
                },
                '503': {
                    'description': '<%= APP_NAME %> is unable to fetch the required resources.'
                }
            }
        }
    }
}
