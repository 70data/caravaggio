# coding=utf-8

from django.urls import path
from .views import status, node, asset, resource

urlpatterns = [
    path('status', status.status, name='status'),
    path('node/downstream/', node.tree_downstream_root, name='tree_node'),
    path('node/downstream/<str:node_name>', node.tree_downstream, name='tree_node'),
    path('node/<str:node_name>', node.tree_node, name='tree_node'),
    path('asset/', asset.tree_asset, name='tree_asset'),
    path('asset/<int:asset_id>', asset.tree_asset_id, name='tree_asset'),
    path('asset/correlation/', asset.tree_correlation_all, name='tree_asset'),
    path('asset/correlation/<str:node_name>', asset.tree_correlation, name='tree_asset'),
    path('asset/<int:asset_id>/resource/', resource.tree_resource_list, name='tree_resource'),
    path('resource/', resource.tree_resource, name='tree_resource'),
    path('resource/<int:resource_id>', resource.tree_resource_id, name='tree_resource'),
]
