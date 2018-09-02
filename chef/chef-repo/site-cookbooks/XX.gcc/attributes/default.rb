case node['my']['fqdn'].split('.')[0]
when /^ai/
  default['my']['gcc'] = {
    'version' => '4.8.5',
    'alternatives' => 'gcc48'
  }
else
end
