##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################
{
    'name' : 'Partner Payment History', # name of your module, search when you need to look it up for installation/updates
    'version' : '4.0', 
    'author' : 'AAG',
    'category' : 'Custom Module', 
    'description' : """ Store customer payment archives """,
    # dependencies--pretty much all modules ought to depend on base; add others if inheriting from them.
    # you'll note in my python script that i do inherit res.partner, but that is a module inside of base so i don't need to include it.
    'depends' : ['base'],  
    'data' : ['partner_payment_view.xml'], # this is the xml view--how the form and tree views should look on the web client 
    'installable': True, 
    'auto_install': False, 
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

