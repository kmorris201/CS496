from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import NewDraftForm, NewHeaderForm, NewTextForm, NewBlankForm, DraftInstanceForm, ToTemplateForm
from .models import LabDraft, LabTemplate, Element

import os, sys, shutil

import reportlab
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

def draft_start (request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name='teachers').exists():

            user = get_object_or_404(User, username = request.user.username)

            drafts = LabDraft.objects.filter(current="True", user = user)

            for draft in drafts:

                draft.current = "False"
                draft.save()

            if request.method == 'POST':

                form1 = NewDraftForm(request.POST)
                form2 = DraftInstanceForm(request.POST, user = request.user)

                if form1.is_valid():

                    title = form1.cleaned_data['title']

                    count = 1

                    file_name = '/home/caleb/Documents/CS496/wku_sims/static/media/lab_repo_drafts/' + title.strip() + request.user.username + str(count)
                    
                    media_path = '/lab_repo_drafts/' + title.strip() + request.user.username + str(count)

                    while os.path.exists(file_name):

                        count = count + 1

                        file_name = '/home/caleb/Documents/CS496/wku_sims/static/media/lab_repo_drafts/' + title.strip() + request.user.username + str(count)
                    
                        media_path = '/lab_repo_drafts/' + title.strip() + request.user.username + str(count)

                    open(file_name, 'w')

                    pdf = canvas.Canvas(file_name)
                    pdf.setTitle(title)

                    text = pdf.beginText()
                    text.setTextOrigin(1.25*inch, 10.44*inch)
                    text.setFont('Times-Bold', 22)
                    text.textLine(title)

                    pdf.drawText(text)

                    text = pdf.beginText()
                    text.setTextOrigin(1.25*inch, 10*inch)
                    text.setFont('Times-Roman', 12)
                    text.textLine('Class:')

                    pdf.drawText(text)

                    text = pdf.beginText()
                    text.setTextOrigin(1.25*inch, 9.7*inch)
                    text.setFont('Times-Roman', 12)
                    text.textLine('Name(s):')

                    pdf.drawText(text)

                    text = pdf.beginText()
                    text.setTextOrigin(1.25*inch, 9.4*inch)
                    text.setFont('Times-Roman', 12)
                    text.textLine('Date:')

                    pdf.drawText(text)

                    pdf.showPage()
                    pdf.save()

                    draft = LabDraft(user = user, title = title, draft = media_path, current = True)

                    draft.save()

                    pk = draft.pk

                    form1 = NewDraftForm()
                    form2 = DraftInstanceForm(user = request.user)

                    return redirect('lab_repo:draft_edit') 

                elif form2.is_valid():
                    
                    selection = form2.cleaned_data['selection']

                    pk = getattr(selection, 'pk')

                    draft = get_object_or_404(LabDraft, pk = pk)

                    draft.current = True

                    draft.save()

                    form1 = NewDraftForm()

                    form2 = DraftInstanceForm(user = request.user)

                    return redirect('lab_repo:draft_edit') 

                else:

                    form1 = NewDraftForm()

                    form2 = DraftInstanceForm(user = request.user)

                    return render(request, 'lab_repo/draft_start.html', {'form1':form1, 'form2':form2})


            else:

                form1 = NewDraftForm()
                
                form2 = DraftInstanceForm(user = request.user)

                return render(request, 'lab_repo/draft_start.html', {'form1':form1, 'form2':form2})
                        

        else:

            return redirect('home:home')

    else:
        
        return redirect('user_extension:login')

def draft_edit(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name='teachers').exists():

            user = get_object_or_404(User, username = request.user.username)

            draft = get_object_or_404(LabDraft, current="True", user = user)

            title = draft.title

            media_path = draft.draft

            file_name = '/home/caleb/Documents/CS496/wku_sims/static/media' + str(media_path)

            os.remove(file_name)

            open(file_name, 'w')

            pdf = canvas.Canvas(file_name)
            pdf.setTitle(title)

            text = pdf.beginText()
            text.setTextOrigin(1.25*inch, 10.44*inch)
            text.setFont('Times-Bold', 22)
            text.textLine(title)

            pdf.drawText(text)

            text = pdf.beginText()
            text.setTextOrigin(1.25*inch, 10*inch)
            text.setFont('Times-Roman', 12)
            text.textLine('Class:')

            pdf.drawText(text)

            text = pdf.beginText()
            text.setTextOrigin(1.25*inch, 9.7*inch)
            text.setFont('Times-Roman', 12)
            text.textLine('Name(s):')

            pdf.drawText(text)

            text = pdf.beginText()
            text.setTextOrigin(1.25*inch, 9.4*inch)
            text.setFont('Times-Roman', 12)
            text.textLine('Date:')

            pdf.drawText(text)

            offset = 9.0

            element = draft.next_element

            element_list = []

            count = 0

            while (element != None):

                element_info = [element.element_type, element.pk]
                element_list.append(element_info)

                count = count + 1

                if (element.element_type == 'header'):

                    if(offset - .5 >= 1):

                        text = pdf.beginText()
                        text.setTextOrigin(1.25*inch, offset*inch)
                        text.setFont('Times-Italic', 16)
                        text.textLine(element.text)
                        pdf.drawText(text)

                        offset = offset - .5

                    else:

                        offset = 10.44

                        pdf.showPage()

                        text = pdf.beginText()
                        text.setTextOrigin(1.25*inch, offset*inch)
                        text.setFont('Times-Italic', 16)
                        text.textLine(element.text)
                        pdf.drawText(text)

                        offset = offset - .5

                elif (element.element_type == 'text'):

                    if(offset - 1 >= 1):

                        text = pdf.beginText()
                        text.setTextOrigin(1.25*inch, offset*inch)
                        text.setFont('Times-Roman', 12)
                        text.textLine(element.text)
                        pdf.drawText(text)

                        offset = offset - 1 

                    else:

                        offset = 10.44

                        pdf.showPage()

                        text = pdf.beginText()
                        text.setTextOrigin(1.25*inch, offset*inch)
                        text.setFont('Times-Roman', 12)
                        text.textLine(element.text)
                        pdf.drawText(text)

                        offset = offset - 1 

                else:

                    if (offset - element.inches_blank >= 1):

                        offset = offset - element.inches_blank

                    else:

                        remaining = (offset - 1 - element.inches_blank) * -1

                        pdf.showPage()

                        offset = 10.44 - remaining

                previous_element = element

                element = element.next_element

            pdf.save()
            
            if count == 0:

                element = draft

            else:

                element = previous_element

            if request.method == 'POST':

                form1 = NewHeaderForm(request.POST)
                form2 = NewTextForm(request.POST)
                form3 = NewBlankForm(request.POST)
                form4 = ToTemplateForm(request.POST)

                if form1.is_valid():

                    text = form1.cleaned_data['header_text']

                    element_type = 'header'

                    header_element = Element(element_type = element_type, text = text)

                    header_element.save()

                    element.next_element = header_element

                    element.save()

                    return redirect('lab_repo:draft_edit')

                elif form2.is_valid():

                    text = form2.cleaned_data['text_text']

                    element_type = 'text'

                    text_element = Element(element_type = element_type, text = text)

                    text_element.save()

                    element.next_element = text_element 

                    element.save()

                    return redirect('lab_repo:draft_edit')

                elif form3.is_valid():

                    inches_blank = form3.cleaned_data['inches_blank']

                    element_type = 'blank'

                    blank_element = Element(element_type = element_type, inches_blank = inches_blank)

                    blank_element.save()

                    element.next_element = blank_element

                    element.save()

                    return redirect('lab_repo:draft_edit')

                elif form4.is_valid():

                    description = form4.cleaned_data['description']

                    temp_count = 1

                    template_name = '/home/caleb/Documents/CS496/wku_sims/static/media/lab_repo_templates/' + title.strip() + request.user.username + str(temp_count)
                    
                    template_path = '/lab_repo_templates/' + title.strip() + request.user.username + str(temp_count)

                    while os.path.exists(template_name):

                        temp_count = temp_count + 1

                        template_name = '/home/caleb/Documents/CS496/wku_sims/static/media/lab_repo_templates/' + title.strip() + request.user.username + str(temp_count)
                    
                        template_path = '/lab_repo_templates/' + title.strip() + request.user.username + str(temp_count)

                    shutil.copy(file_name, template_name)

                    os.remove(file_name)

                    draft.delete()

                    template = LabTemplate(user = user, description = description, title = title, template = template_path)

                    template.save()

                    return redirect('lab_repo:draft_start')

                else:

                    form1 = NewHeaderForm()
                    form2 = NewTextForm()
                    form3 = NewBlankForm()
                    form4 = ToTemplateForm()

                    return render(request, 'lab_repo/draft_edit.html', {'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4, 'element_list':element_list, 'title':title, 'media_path':media_path})

            else:

                form1 = NewHeaderForm()
                form2 = NewTextForm()
                form3 = NewBlankForm()
                form4 = ToTemplateForm()

                return render(request, 'lab_repo/draft_edit.html', {'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4, 'element_list':element_list, 'title':title, 'media_path':media_path})

        else:

            return redirect('home:home')

    else:

        return redirect('user_extension:login')

def element_delete(request, pk):

    if request.user.is_authenticated:

        if request.user.groups.filter(name='teachers').exists():

            user = get_object_or_404(User, username = request.user.username)

            draft = get_object_or_404(LabDraft, current="True", user = user)

            to_delete = get_object_or_404(Element, pk=pk)

            element = draft

            while (element.next_element != None and element.next_element != to_delete):
                element = element.next_element


            new_next = None

            if to_delete.next_element != None:

                new_next = to_delete.next_element

            
            to_delete.delete()

            element.next_element = new_next

            element.save()

            return redirect('lab_repo:draft_edit')

        else:


            return redirect('home:home')

    else:

        return redirect('user_extension:login')

def draft_delete(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name='teachers').exists():

            user = get_object_or_404(User, username = request.user.username)

            draft = get_object_or_404(LabDraft, current="True", user = user)

            path = "/home/caleb/Documents/CS496/wku_sims/static/media" + str(draft.draft)

            draft.delete()

            os.remove(path)

            return redirect('lab_repo:draft_start')

        else:

            return redirect('home:home')

    else:

        return redirect('user_extension:login')
