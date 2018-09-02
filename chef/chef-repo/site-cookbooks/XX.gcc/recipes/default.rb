#
# Cookbook Name:: XX.gcc
# Recipe:: default
#
# Copyright 2018, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#
#

#bash "hoge" do
#  code "alternatives --set gcc /usr/bin/gcc48"
#end
#
#

#if node['languages']['c']['gcc']['version'] != node['my']['gcc']['version'] 
#  execute "hoge" do
#    command "alternatives --set gcc /usr/bin/#{node['my']['gcc']['alternatives']}"
#  end
#end


execute "hoge" do
  command "alternatives --set gcc /usr/bin/#{node['my']['gcc']['alternatives']}"
  not_if " gcc --version 2>&1 | egrep -q '#{node['my']['gcc']['version']}' "
end
