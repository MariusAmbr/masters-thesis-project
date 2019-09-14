<?php


namespace App\Form;

use PlumTreeSystems\FileBundle\Form\Type\PTSFileType;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\CheckboxType;
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\FormBuilderInterface;

class NewSegmentationDataType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options)
    {
        $builder
            ->add('image', PTSFileType::class, [
                'multiple' => false
            ])
            ->add('maskedImage', PTSFileType::class, [
                'multiple' => false
            ])
            ->add('enabled', CheckboxType::class)
        ;
    }
}