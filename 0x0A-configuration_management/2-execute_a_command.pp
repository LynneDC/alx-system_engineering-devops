## executes external command from shell
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
