# Killing killmenow process
exec { 'pkill killmenow':
    path => '/usr/bin'
}
