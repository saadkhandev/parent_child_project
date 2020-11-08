#parent_child_project

#### Download or pull the project from : git@github.com:saadkhandev/parent_child_project.git

## Base url: http://127.0.0.1:8000/api/v1/

By using the following endpoint, URL is formed by baseurl + endpoint and API communication is performed.


## Main endpoints

| Endpoint name       |  Link                | Method|  Purpose                      |  
|---------------------|----------------------|-------|-------------------------------|
|  SignIn             | /signin              | POST  | For login into system         | 
|  Get User Dashboard | /user/<int:user_id>  | GET   | For user Dashboard            |  
|  SignUp             | /user/registration   | POST  | For student/teacher           |  
|  Active Users       | /active-account      | POST  | Active registered users       |   
|  Signout            | /signout             | POST  | Signout users                 |   


  



##### Sample response list for Whole project:

1. HTTP_201_CREATED
2. HTTP_400_BAD_REQUEST
3. HTTP_401_UNAUTHORIZED
4. HTTP_403_FORBIDDEN
5. HTTP_415_UNSUPPORTED_MEDIA_TYPE
6. HTTP_409_CONFLICT
7. HTTP_404_NOT_FOUND
8. HTTP_204_NO_CONTENT
9. HTTP_500_INTERNAL_SERVER_ERROR
10. HTTP_200_OK



### HTTP REQUEST :  **POST  /signin**

###### params
```json
{	
	"email" : "sisomow776@elesb.net",
	"password" : "333333"
}
```

| parameter   | is required | comment       |
|  ---------  | ----------  |  -----------  |
| email       | true        |               |
| password    | true        |               |
