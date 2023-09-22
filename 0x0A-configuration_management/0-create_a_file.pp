## create a file with these attr
file { '//tmp/school':
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'echo I love Puppet',
}
