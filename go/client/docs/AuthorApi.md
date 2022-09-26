# {{classname}}

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AuthorGet**](AuthorApi.md#AuthorGet) | **Get** /author | Fetch ISBN list of authors works

# **AuthorGet**
> []Isbn AuthorGet(ctx, author)
Fetch ISBN list of authors works

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **author** | [**string**](.md)|  | 

### Return type

[**[]Isbn**](ISBN.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/'json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

